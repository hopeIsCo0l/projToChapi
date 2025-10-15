// API Configuration - Dynamic based on current hostname
export const getApiBaseUrl = (): string => {
  if (typeof window === 'undefined') {
    // Server-side rendering - use environment variable or default
    return process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';
  }
  
  // Client-side - check current hostname
  const hostname = window.location.hostname;
  const protocol = window.location.protocol;
  
  if (hostname === '172.16.149.71') {
    // Accessing via WiFi IP
    return 'http://172.16.149.71:8000';
  } else if (hostname === 'localhost' || hostname === '127.0.0.1') {
    // Local development
    return 'http://localhost:8000';
  } else if (hostname.includes('railway.app') || hostname.includes('vercel.app') || hostname.includes('netlify.app')) {
    // Production deployment - use environment variable or construct URL
    const apiUrl = process.env.NEXT_PUBLIC_API_URL;
    if (apiUrl) {
      return apiUrl;
    }
    // Fallback: construct API URL from current hostname
    return `${protocol}//${hostname.replace('frontend-', 'backend-')}`;
  } else {
    // Fallback to environment variable or localhost
    return process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';
  }
};

export const getApiEndpoints = () => {
  const baseUrl = getApiBaseUrl();
  return {
    WAITLIST_SIGNUP: `${baseUrl}/api/v1/waitlist/signup`,
    ADMIN_ENTRIES: `${baseUrl}/api/v1/admin/entries`,
  };
};

// For backward compatibility
export const API_ENDPOINTS = getApiEndpoints();
export default getApiBaseUrl();
