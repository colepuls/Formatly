#!/bin/bash

echo "🚀 Formatly Deployment Script"
echo "=============================="

# Check if git is initialized
if [ ! -d ".git" ]; then
    echo "📁 Initializing git repository..."
    git init
    git add .
    git commit -m "Initial commit"
fi

echo "📦 Preparing for deployment..."

# Create .gitkeep files if they don't exist
mkdir -p uploads outputs
touch uploads/.gitkeep outputs/.gitkeep

# Add all files
git add .

# Check if there are changes to commit
if git diff --staged --quiet; then
    echo "✅ No changes to commit"
else
    echo "💾 Committing changes..."
    git commit -m "Update for deployment"
fi

echo ""
echo "🎯 Choose your deployment platform:"
echo "1. Heroku"
echo "2. Railway"
echo "3. Render"
echo "4. DigitalOcean App Platform"
echo "5. Local production server"
echo ""

read -p "Enter your choice (1-5): " choice

case $choice in
    1)
        echo "🚀 Deploying to Heroku..."
        if ! command -v heroku &> /dev/null; then
            echo "❌ Heroku CLI not found. Please install it first:"
            echo "   https://devcenter.heroku.com/articles/heroku-cli"
            exit 1
        fi
        
        read -p "Enter your Heroku app name: " app_name
        heroku create $app_name
        git push heroku main
        heroku open
        ;;
    2)
        echo "🚂 Deploying to Railway..."
        echo "✅ Push your code to GitHub and connect to Railway:"
        echo "   https://railway.app/"
        ;;
    3)
        echo "🎨 Deploying to Render..."
        echo "✅ Push your code to GitHub and connect to Render:"
        echo "   https://render.com/"
        ;;
    4)
        echo "🌊 Deploying to DigitalOcean App Platform..."
        echo "✅ Push your code to GitHub and connect to DigitalOcean:"
        echo "   https://www.digitalocean.com/products/app-platform"
        ;;
    5)
        echo "🏠 Starting local production server..."
        echo "📦 Installing production dependencies..."
        pip install gunicorn
        echo "🚀 Starting server with gunicorn..."
        gunicorn wsgi:app --bind 0.0.0.0:5001 --workers 4
        ;;
    *)
        echo "❌ Invalid choice"
        exit 1
        ;;
esac

echo ""
echo "🎉 Deployment complete!"
echo "📖 Check the README.md for detailed instructions" 