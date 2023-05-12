import TokenManager from "@/managers/TokenManager";

export default function authHeader() {
  let token = TokenManager.getToken();

  if (token) {
    return { Authorization: `Bearer ${token.access}` };
  } else {
    return {};
  }
}
