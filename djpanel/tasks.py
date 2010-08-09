from celery.decorators import task

@task
def run_block(block_name, block_configuration, cache_unique):
	#get block
	#configure block
	#run block
	#save response in cache
	#send response on channel
	pass