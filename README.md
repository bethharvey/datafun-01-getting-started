# datafun-01-getting-started

## Beth's Saved Notes
After installing VS Code editor, Python extension, and GitHub Repositories extension
To fork a repo in GitHub, click Fork button at top, click 'Create Fork'
To clone a GitHub repo in VS Code:
1. Open VS Code. 
1. From the menu: select View / Command Palette.
1. Start typing Git: Clone and select it.
1. Provide the URL of **your** new GitHub repo.
1. Select desired location.

For more information about options for executing a Python program in VS Code, see [Run Hello World](https://code.visualstudio.com/docs/python/python-tutorial#_run-hello-world).

The about module provides a lot of useful information about your Python environment. 
Review these paths carefully - it tells a lot about your Python installation and environment. 

To commit changes and push to GitHub:

1. On the VS Code side panel, click the source control icon (look for a blue bubble with an number in it).
1. Important! Above the Commit button, it will say "Message". You must include a message. 
1. In that message input box, type "initial setup".
1. Click the blue "Commit" button and follow instructions to Commit your code and sync/push it up to your GitHub repo. 

If your computer hangs because you forget the a commit message, 
just enter your message in the top line of the file it shows in the editor.
Then click the checkmark in the upper right to close that file and save your commit message.
"Sync your changes" to push. 

If we didn't use VS Code, the commands are pretty easy in Git Bash or Terminal as well:

```
git add .
git commit -m "initial setup"
git push origin main
```

## Checklist

Change the open boxes [ ] below to checked boxes [x] as you complete the tasks.

- [x] Task 1. Sign up for GitHub
- [x] Task 2. Install (and configure) Git
- [x] Task 3. Install Miniconda3 (or other)
- [x] Task 4. Install VS Code
- [x] Task 5. Install VS Code Extension: Python
- [x] Task 6. Install VS Code Extension: GitHub Repositories
- [x] Task 7. Fork this repo into your account
- [x] Task 8. Clone your new GitHub repo down
- [x] Task 9. Explore the repo in VS Code
- [x] Task 10. Execute a Python script.
- [x] Task 11. Check the boxes (edit a Markdown file)
- [x] Task 12. Commit changes (with a message!) and push to GitHub

Finally - after your initial commit and push, you can check the last box. 
Check the box, commit your changes (with a message!), and push/sync again. 

## Tips and Troubleshooting

### Issue: VS Code - No Source Control Icon

Suggestion: If you're in VS Code, and you don't see the Source Control icon with a blue bubble, right-click on the sidebar icons, and make sure "Source Control" is checked.  

### Issue: VS Code - Conda Error on Execute

Suggestion: If you're in VS Code, On Windows, trying to run a script or execute a conda command and you get an error "conda: The term 'conda' is not recognized as a name of a cmdlet, function, script file, or executable program." Your VS Code terminal is likely Powershell (look for a the PS before your path). We want to switch it to "Command Prompt" for Python commands. From the VS Code menu / View / Command Palette. Start typing 'Terminal: Select Default Profile' until it appears, click it and change from Powershell to Command Prompt.

### Issue: VS Code wants to install Pylance extension

Suggestion: Sure. If VS Code suggests an extension, it's often good to go ahead and try it. 
Read up a bit if curious, but the suggestions are usually helpul. 

### Issue: VS Code Extension for GitHub - which one?

Suggestion: VS Code Extension: [GitHub Repositories](https://marketplace.visualstudio.com/items?itemName=GitHub.remotehub) seems to work well and may especially good for beginners. 
If you get a recommendation to use [GitHub Pull Requests and Issues](https://marketplace.visualstudio.com/items?itemName=GitHub.vscode-pull-request-github), you can try that. It might be more suitable for experienced developers. [Here's a good article for getting started](https://www.techrepublic.com/article/add-github-vs-code/). You're encouraged to share your thoughts in the discussions.

## Additional Resources

1. For more information about editing Markdown task lists, see [how to mark a task complete](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/about-task-lists).

1. For more information about Git in VS Code, see [Using Git source control in VS Code](https://code.visualstudio.com/docs/sourcecontrol/overview).

1. For more information about editing Markdown in VS Code, see [Markdown and Visual Studio Code](https://code.visualstudio.com/docs/languages/markdown).

