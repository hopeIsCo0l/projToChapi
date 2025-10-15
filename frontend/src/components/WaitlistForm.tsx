'use client';

import { useState, useEffect } from 'react';
import { getApiEndpoints } from '@/config/api';

interface FormState {
  email: string;
  isLoading: boolean;
  message: string;
  isSuccess: boolean;
}

export function WaitlistForm() {
  const [state, setState] = useState<FormState>({
    email: '',
    isLoading: false,
    message: '',
    isSuccess: false
  });

  // Auto-clear success message after 5 seconds
  useEffect(() => {
    if (state.isSuccess && state.message) {
      const timer = setTimeout(() => {
        setState(prev => ({ ...prev, message: '' }));
      }, 5000);
      return () => clearTimeout(timer);
    }
  }, [state.isSuccess, state.message]);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    
    if (!state.email) {
      setState(prev => ({
        ...prev,
        message: 'Please enter your email address',
        isSuccess: false
      }));
      return;
    }

    setState(prev => ({ ...prev, isLoading: true, message: '' }));

    try {
      const apiEndpoints = getApiEndpoints();
      const response = await fetch(apiEndpoints.WAITLIST_SIGNUP, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ email: state.email }),
      });

      const data = await response.json();

      if (response.ok) {
        setState(prev => ({
          ...prev,
          isLoading: false,
          message: data.message,
          isSuccess: true,
          email: ''
        }));
      } else {
        setState(prev => ({
          ...prev,
          isLoading: false,
          message: data.detail || 'Something went wrong. Please try again.',
          isSuccess: false
        }));
      }
    } catch (error) {
      console.error('Waitlist signup error:', error);
      const apiEndpoints = getApiEndpoints();
      setState(prev => ({
        ...prev,
        isLoading: false,
        message: `Network error. Please check your connection and try again. (API: ${apiEndpoints.WAITLIST_SIGNUP})`,
        isSuccess: false
      }));
    }
  };

  const handleEmailChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setState(prev => ({
      ...prev,
      email: e.target.value,
      message: ''
    }));
  };

  // Debug info (only show in development)
  const apiEndpoints = getApiEndpoints();
  
  return (
    <div className="space-y-6">
      {/* Debug info - only show in development */}
      {process.env.NODE_ENV === 'development' && (
        <div className="text-xs text-gray-500 dark:text-gray-400 bg-gray-100 dark:bg-gray-800 p-2 rounded">
          Debug: API endpoint: {apiEndpoints.WAITLIST_SIGNUP}
        </div>
      )}
      
      <form onSubmit={handleSubmit} className="space-y-4">
        {/* Email Input */}
        <div className="relative">
          <div className="absolute inset-y-0 left-0 pl-4 flex items-center pointer-events-none">
            <svg className="h-5 w-5 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M16 12a4 4 0 10-8 0 4 4 0 008 0zm0 0v1.5a2.5 2.5 0 005 0V12a9 9 0 10-9 9m4.5-1.206a8.959 8.959 0 01-4.5 1.207" />
            </svg>
          </div>
          <input
            type="email"
            id="email"
            value={state.email}
            onChange={handleEmailChange}
            disabled={state.isLoading}
            className="w-full pl-12 pr-4 py-4 bg-gray-50/50 dark:bg-gray-700/50 border border-gray-200 dark:border-gray-600 rounded-xl focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 disabled:bg-gray-100 dark:disabled:bg-gray-800 disabled:cursor-not-allowed transition-all duration-200 text-gray-900 dark:text-white placeholder-gray-500 dark:placeholder-gray-400"
            placeholder="Enter your email address"
            required
          />
        </div>

        {/* Submit Button */}
        <button
          type="submit"
          disabled={state.isLoading || !state.email.trim()}
          className="w-full relative overflow-hidden bg-gradient-to-r from-indigo-600 to-purple-600 hover:from-indigo-700 hover:to-purple-700 text-white py-4 px-6 rounded-xl font-semibold text-lg shadow-lg hover:shadow-xl disabled:opacity-50 disabled:cursor-not-allowed transition-all duration-300 transform hover:scale-[1.02] active:scale-[0.98]"
        >
          <span className="relative z-10 flex items-center justify-center">
            {state.isLoading ? (
              <>
                <svg className="animate-spin -ml-1 mr-3 h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                  <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                  <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                </svg>
                Joining...
              </>
            ) : (
              <>
                <svg className="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13 7l5 5m0 0l-5 5m5-5H6" />
                </svg>
                Join Waitlist
              </>
            )}
          </span>
          {/* Button shine effect */}
          <div className="absolute inset-0 -top-2 -left-2 bg-gradient-to-r from-transparent via-white/20 to-transparent skew-x-12 transform translate-x-[-100%] group-hover:translate-x-[200%] transition-transform duration-700"></div>
        </button>
      </form>

      {/* Status Message */}
      {state.message && (
        <div className={`relative overflow-hidden rounded-xl p-4 border-l-4 animate-fade-in ${
          state.isSuccess 
            ? 'bg-green-50 dark:bg-green-900/20 text-green-800 dark:text-green-200 border-green-500' 
            : 'bg-red-50 dark:bg-red-900/20 text-red-800 dark:text-red-200 border-red-500'
        }`}>
          <div className="flex items-center">
            <div className="flex-shrink-0">
              {state.isSuccess ? (
                <svg className="h-5 w-5 text-green-500" fill="currentColor" viewBox="0 0 20 20">
                  <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clipRule="evenodd" />
                </svg>
              ) : (
                <svg className="h-5 w-5 text-red-500" fill="currentColor" viewBox="0 0 20 20">
                  <path fillRule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7 4a1 1 0 11-2 0 1 1 0 012 0zm-1-9a1 1 0 00-1 1v4a1 1 0 102 0V6a1 1 0 00-1-1z" clipRule="evenodd" />
                </svg>
              )}
            </div>
            <div className="ml-3">
              <p className="text-sm font-medium">{state.message}</p>
            </div>
          </div>
        </div>
      )}

      {/* Success Animation */}
      {state.isSuccess && (
        <div className="fixed inset-0 pointer-events-none z-50 flex items-center justify-center">
          <div className="bg-green-500 text-white px-6 py-3 rounded-full shadow-lg animate-bounce-subtle">
            <div className="flex items-center">
              <svg className="w-5 h-5 mr-2" fill="currentColor" viewBox="0 0 20 20">
                <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clipRule="evenodd" />
              </svg>
              Welcome to the waitlist!
            </div>
          </div>
        </div>
      )}
    </div>
  );
}


