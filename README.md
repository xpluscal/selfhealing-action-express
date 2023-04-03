> :warning: **Experimental repository**: This is an experimental repository for research and educational purposes only, use at your own risk. I do not take any liability for any damage caused by this repository.

# selfhealing-action-express
Demo experimental repository of a self-healing code GitHub action pipeline using [Langchain](https://github.com/hwchase17/langchain) and [Openai](https://openai.com/).

The workflow action is language agnostic and works on single file errors only for now.

## What is this?
The repository is a simple express typescript server with a github workflow action that triggers the healing process when the build action fails.

## How does it work?

The workflow action is triggered when a push is made to the repository. The action runs the build script and if it fails, it triggers the healing process. The healing process runs an LLM chain to determine:

1. Where the error is
2. What the error is
3. What the fix is
4. Writes the fix to the file

Then it commits the changes back to the repository.

## Where could this go from here?
This should be treated as an early experimental prototype and currently works on single files only. The next steps could be to:

<!-- checkmark -->
- [ ] Create embeddings of dependencies and use them to determine the correct file to fix (e.g. by passing the relevant context via Vector Similarity Search from a vector DB)
- [ ] Add support for multiple / recursive file detections and errors
- [ ] Add support for retry limits to avoid the infinite loop when no fixes can be found
- [ ] Change workflow to instead of commiting to the branch directly, have the AI commit to a new branch and then create a pull request and assign to the original committer for review
- [ ] Add better test support

## Contributing
If you would like to contribute to this project, please feel free to open a pull request or issue.