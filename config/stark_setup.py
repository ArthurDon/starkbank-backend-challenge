import starkbank

starkbank.user = starkbank.Project(
    id="6309923013001216",
    private_key=open("keys/private-key.pem").read(),
    environment="sandbox"
)
