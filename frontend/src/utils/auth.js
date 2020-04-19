export function getToken() {
  return localStorage.getItem('access_token')
}

export function setToken(token) {
  return localStorage.setItem('access_token', token)
}

export function removeToken() {
  return localStorage.removeItem('access_token')
}
