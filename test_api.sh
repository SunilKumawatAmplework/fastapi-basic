#!/bin/bash

echo "🚀 Testing FastAPI Endpoints"
echo "=============================="
echo ""

# Test 1: Root endpoint
echo "1️⃣  Testing Root Endpoint (GET /)"
curl -X GET http://localhost:8000/
echo -e "\n"

# Test 2: Create User
echo "2️⃣  Testing Create User (POST /user/)"
curl -X POST http://localhost:8000/user/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "testuser",
    "email": "test@example.com",
    "password": "testpassword123"
  }'
echo -e "\n"

# Test 3: Create User with Long Password
echo "3️⃣  Testing Create User with Long Password (POST /user/)"
curl -X POST http://localhost:8000/user/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "testuser2",
    "email": "test2@example.com",
    "password": "this_is_a_very_long_password_that_exceeds_72_bytes_and_should_be_truncated_automatically_by_our_hash_function"
  }'
echo -e "\n"

echo "✅ Tests Complete!"
echo ""
echo "💡 You can also visit http://localhost:8000/docs for interactive API documentation"
