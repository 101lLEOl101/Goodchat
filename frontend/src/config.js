const trimTrailingSlash = (value) => value.replace(/\/+$/, "");

const apiBaseUrl = trimTrailingSlash(
  process.env.VUE_APP_API_BASE_URL || "http://localhost:8000/api"
);

export const API_BASE_URL = apiBaseUrl;
export const API_URL = `${apiBaseUrl}/`;
export const API_ORIGIN = apiBaseUrl.replace(/\/api$/, "");
