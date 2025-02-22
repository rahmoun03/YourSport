FROM node:18-alpine AS builder

# Set working directory
WORKDIR /app

# Copy package.json and install dependencies
COPY package.json package-lock.json ./
RUN npm install

# Copy the rest of the app
COPY . .

# Build the Next.js app
RUN npm run build

# Production image
FROM node:18-alpine
WORKDIR /app

# Copy build files from the builder stage
COPY --from=builder /app ./

# Install only production dependencies
RUN npm ci --omit=dev

# Expose the port
EXPOSE 3000

# Start the Next.js app
CMD ["npm", "start"]
