from pyngrok import ngrok

if __name__ == "__main__":
    ngrok.kill()
    access_token = input("input your ngrok access token: ")
    domain = input("input your ngrok domain name: ")
    ngrok.set_auth_token(access_token) 
    ngrok_tunnel = ngrok.connect(addr="5000", proto="http", bind_tls=True, 
                                domain=domain)

    print("MLflow UI ", ngrok_tunnel.public_url)