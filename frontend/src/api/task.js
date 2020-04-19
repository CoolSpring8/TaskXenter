import request from '@/utils/request'

export function fetchList(query) {
  return request({
    url: '/api/tasks/all',
    method: 'get',
    params: query
  })
}

export function fetchTask(id) {
  return request({
    url: '/api/tasks/detail',
    method: 'get',
    params: { id }
  })
}

export function createTask(data) {
  return request({
    url: '/api/tasks/create',
    method: 'post',
    data
  })
}

export function updateTask(data) {
  return request({
    url: '/api/tasks/update',
    method: 'post',
    data
  })
}
