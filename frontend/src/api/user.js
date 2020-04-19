import request from '@/utils/request'

export function login(data) {
  return request({
    url: '/api/user/token',
    method: 'post',
    data
  })
}

export function getMyInfo(token) {
  return request({
    url: '/api/user/me',
    method: 'get'
  })
}

export function logout() {
}
