FROM node:18-alpine AS build

WORKDIR /app

ARG VUE_APP_API_BASE_URL=http://localhost:8000/api
ARG VUE_APP_SITE_URL=http://localhost:3000
ENV VUE_APP_API_BASE_URL=$VUE_APP_API_BASE_URL
ENV VUE_APP_SITE_URL=$VUE_APP_SITE_URL

COPY package.json package-lock.json ./
RUN npm ci --no-audit --no-fund

COPY . .
RUN npm run build

FROM nginx:1.27-alpine AS runtime

COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=build /app/dist /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
