export const API_PROTOCOL = process.env.PROTOCOL ? process.env.PROTOCOL : 'http://';
export const API_DOMAIN = process.env.API_DOMAIN ? `${API_PROTOCOL}${process.env.API_DOMAIN}` : `${API_PROTOCOL}localhost:8000/`;
export const API_PATH = process.env.API_PATH ? process.env.API_PATH : 'api/';

// Auth
export const SIGNIN_API_PATH = () => `${API_PATH}api-token-auth/`;
export const SIGNIN_API_URL = () => `${API_DOMAIN}${SIGNIN_API_PATH()}`;
