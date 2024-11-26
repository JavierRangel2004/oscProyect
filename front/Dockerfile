# front/Dockerfile

# Usa una imagen base de Node.js
FROM node:18-alpine

# Establece el directorio de trabajo
WORKDIR /usr/src/app

# Copia los archivos de dependencias
COPY package.json package-lock.json ./

# Instala Angular CLI globalmente y luego las dependencias del proyecto
RUN npm install -g @angular/cli@latest && npm install

# Copia el resto del código de la aplicación
COPY . .

# Exponer el puerto que usará Angular
EXPOSE 4200

# Comando para iniciar el servidor de desarrollo de Angular
CMD ["ng", "serve", "--host", "0.0.0.0", "--poll", "2000"]
