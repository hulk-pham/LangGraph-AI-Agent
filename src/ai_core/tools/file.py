from tempfile import TemporaryDirectory

from langchain_community.agent_toolkits import FileManagementToolkit

# We'll make a temporary directory to avoid clutter
working_directory = TemporaryDirectory()

file_toolkit = FileManagementToolkit(
    root_dir=str(working_directory.name)
)

file_toolkit.get_tools()