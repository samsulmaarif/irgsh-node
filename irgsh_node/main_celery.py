import os

def main():
    import amqplib_sslcert_patch
    amqplib_sslcert_patch.use_configured_cert()

    os.environ.setdefault('IRGSH_NODE_COFNIG', 'irgsh-node.conf')
    os.environ.setdefault('CELERY_LOADER', 'irgsh_node.loader.IrgshNodeLoader')

    from celery.bin import celeryd
    celeryd.main()

if __name__ == '__main__':
    main()

