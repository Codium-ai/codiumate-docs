import hashlib


def compute_hash(input_string):
	#Convert the input string to bytes
	input_bytes = input_string.encode('utf-8')

	#Create a SHA-256 hash object
	hash_object = hashlib.sha256(input_bytes)

	#Compute the hash and return it as a hexadecimal string
	return hash_object.hexdigest()


#Example usage
"""
      - name: Clone pr-agent-pro repo
        uses: actions/checkout@v2
        with:
          repository: Codium-ai/pr-agent-pro
          ref: main
          path: pr-agent-pro
          ssh-key: ${{ secrets.PR_AGENT_PRO_SSH_KEY }}
"""