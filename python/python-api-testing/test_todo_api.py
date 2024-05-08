import requests
import uuid

BASE_URL= 'https://todo.pixegami.io/'

def create_task(payload):
    return requests.put(BASE_URL+'/create-task', json=payload)

def get_task(task_id):
    return requests.get(BASE_URL+'/get-task/'+task_id)

def new_task_payload():
    return {
        "content": "my test content",
        "user_id": "test user-id",
        "is_done": False
    }

def update_task(payload):
    return requests.put(BASE_URL+'/update-task/', json=payload)

def list_tasks(user_id):
    return requests.get(BASE_URL+'/list-tasks/'+user_id)

def delete_task(task_id):
    return requests.delete(BASE_URL+'/delete-task/'+task_id)

def test_can_call_endpoint():
    response = requests.get(BASE_URL)
    assert response.status_code == 200

def test_can_create_task():
    payload= new_task_payload()
    create_task_response = create_task(payload)
    assert create_task_response.status_code == 200
    data = create_task_response.json()
    
    # get the task_id that was created
    task_id = data['task']['task_id']

    get_task_response = get_task(task_id)
    assert get_task_response.status_code == 200
    data = get_task_response.json()
        
    assert data['content'] == payload['content']
    assert data['user_id'] == payload["user_id"]
    assert data['is_done'] == payload["is_done"]

def test_fail_to_create_task():
    payload= {
        "content": 'my test content',
        "user_id": "test user-id",
        "task_id": "test task-id",
        "is_done": 123
    }
    response = requests.put(BASE_URL+'/create-task', json=payload)
    failure_message = {
        'message': 'value could not be parsed to a boolean',
        'error_type': 'type_error.bool'
    }
    assert response.status_code == 422
    data = response.json()
    
    assert data['detail'][0]['msg'] == failure_message['message']
    assert data['detail'][0]['type'] == failure_message['error_type']

def test_can_update_task():
    #create task
    payload = new_task_payload()
    create_task_response = create_task(payload)
        
    # get the task_id that was created
    task_id = create_task_response.json()['task']['task_id']
    #update task
    new_payload = {
        'user_id': payload['user_id'],
        'task_id': task_id,
        'content': 'new content',
        'is_done': True
    }
    update_task_response = update_task(new_payload)
    assert update_task_response.status_code == 200
    # get and validate changes
    get_task_response = get_task(task_id)
    assert get_task_response.status_code == 200
    data = get_task_response.json()
    assert data['content'] == new_payload['content']
    assert data['is_done'] == new_payload['is_done']

def test_can_list_tasks():
    # Create a random user_id
    random_user_id = 'test_'+uuid.uuid4().hex
    # Create a task payload with the random user_id
    payload = {
        "content": "my test content",
        "user_id": random_user_id,
        "is_done": False
        }
    # Create N tasks
    n = 4
    for i in range(n):
        create_task_response = create_task(payload)
        assert create_task_response.status_code == 200
    # Get list of tasks
    list_tasks_response = list_tasks(payload['user_id'])
    assert list_tasks_response.status_code == 200
    data = list_tasks_response.json()
    # Validates that the number of tasks match
    assert len(data['tasks']) == n

def test_can_delete_task():
    payload = new_task_payload()
    create_task_response = create_task(payload)
    assert create_task_response.status_code == 200
    task_id = create_task_response.json()['task']['task_id']

    delete_task_response = delete_task(task_id)
    assert delete_task_response.status_code == 200
    get_task_response = get_task(task_id)
    assert 'not found' in get_task_response.json()['detail'] 
    
