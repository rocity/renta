export const API_PROTOCOL = process.env.PROTOCOL ? process.env.PROTOCOL : 'http://';
export const API_DOMAIN = process.env.API_DOMAIN ? `${API_PROTOCOL}${process.env.API_DOMAIN}` : `${API_PROTOCOL}localhost:8000/`;
export const API_PATH = process.env.API_PATH ? process.env.API_PATH : 'api/';

// Auth
export const SIGNIN_API_PATH = () => `${API_PATH}api-token-auth/`;
export const SIGNIN_API_URL = () => `${API_DOMAIN}${SIGNIN_API_PATH()}`;

// Profile
export const PROFILE_API_PATH = () => `${API_PATH}profiles/`;
export const PROFILE_API_URL = () => `${API_DOMAIN}${PROFILE_API_PATH()}`;

export const PROFILE_OWN_API_PATH = () => `${API_PATH}profiles/own/`;
export const PROFILE_OWN_API_URL = () => `${API_DOMAIN}${PROFILE_OWN_API_PATH()}`;

// Listings
export const LISTINGS_API_PATH = (id=null) => `${API_PATH}listings/${id ? `${id}/` : ''}`;
export const LISTINGS_API_URL = (id=null) => `${API_DOMAIN}${LISTINGS_API_PATH(id)}`;
