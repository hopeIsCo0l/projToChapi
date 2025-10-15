import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  output: 'standalone',
  // Enable static exports for Railway
  trailingSlash: true,
  images: {
    unoptimized: true,
  },
};

export default nextConfig;
