# smb-test

This repo contains a basic example of how to use the `smbprotocol` module. I am also using the `dotenv` module to set default values for the environment variables that the example expects.

## How to use

This example was created using Python3. To install the dependencies run: `pip3 install -r dependencies.txt`. You will also need to either export the following environment variables, or add them to a file called `.env`. Exporting is easy, e.g.:

```
$ export SMB_PASSWORD=password
```

Using the .env file is also easy, e.g.:

```
SMB_PASSWORD='password'
```

The script will look for exported environment variables first, and fall back to the contents of the .env file if not found

Once the dependencies are installed and the environment set up you can run the script with `python3 app.py`

That's all goodbye :)
