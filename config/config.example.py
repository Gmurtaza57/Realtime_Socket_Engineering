config = {
    "openai": {
        "api_key": "OPENAI_KEY"
    },
    "kafka": {
        "sasl.username": "",
        "sasl.password": "",
        "bootstrap.servers": "",
        'security.protocol': 'SASL_SSL',
        'sasl.mechanisms': 'PLAIN',
        'session.timeout.ms': 45000
    },
    "schema_registry": {
        "url": "",
        "basic.auth.user.info": "username:password"
    }
}