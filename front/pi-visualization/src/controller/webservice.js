import axios from "axios";

export const webservice = (url) => {
  let instance = axios.create({
    baseURL: url || 'http://127.0.0.1:5000',
  })

  return instance
}