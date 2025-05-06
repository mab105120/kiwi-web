from flask import Flask
from flask_cors import CORS
from app.config import Config
from app.extensions import db
from app.routes.user_routes import user_bp
from app.routes.portfolio_routes import portfolio_bp
from app.routes.investment_routes import investment_bp

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(Config)
    db.init_app(app)

    app.register_blueprint(user_bp, url_prefix='/user')
    app.register_blueprint(portfolio_bp, url_prefix='/portfolio')
    app.register_blueprint(investment_bp, url_prefix='/investment')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)