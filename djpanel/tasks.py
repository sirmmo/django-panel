from celery.decorators import task

@task
def run_block(block_name, block_configuration, cache_unique):
	pass