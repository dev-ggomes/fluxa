// The module 'vscode' contains the VS Code extensibility API
// Import the module and reference it with the alias vscode in your code below
import * as vscode from 'vscode';

// This method is called when your extension is activated
// Your extension is activated the very first time the command is executed
export function activate(context: vscode.ExtensionContext) {

	// Use the console to output diagnostic information (console.log) and errors (console.error)
	// This line of code will only be executed once when your extension is activated
	console.log('Congratulations, your extension "fluxa-language" is now active!');

	// The command has been defined in the package.json file
	// Now provide the implementation of the command with registerCommand
	// The commandId parameter must match the command field in package.json
	const disposable = vscode.commands.registerCommand('fluxa-language.helloWorld', () => {
		// The code you place here will be executed every time your command is executed
		// Display a message box to the user
		vscode.window.showInformationMessage('Hello World from fluxa-language!');
	});

	context.subscriptions.push(disposable);

	vscode.languages.registerCompletionItemProvider('fluxa', {
		provideCompletionItems(document, position) {
			const suggestions = [
				{
					label: 'print',
					kind: vscode.CompletionItemKind.Keyword,
					insertText: 'print()',
				},
				{
					label: 'func',
					kind: vscode.CompletionItemKind.Keyword,
					insertText: 'func name() {\n\t$0\n}',
				},
				{
					label: 'def',
					kind: vscode.CompletionItemKind.Keyword,
					insertText: 'def name() {\n\t$0\n}',
				},
				{
					label: 'if',
					kind: vscode.CompletionItemKind.Keyword,
					insertText: 'if (condition) {\n\t$0\n}',
				},
				{
					label: 'else',
					kind: vscode.CompletionItemKind.Keyword,
					insertText: 'else {\n\t$0\n}',
				},
				{
					label: 'for',
					kind: vscode.CompletionItemKind.Keyword,
					insertText: 'for (variable in list) {\n\t$0\n}',
				},
				{
					label: 'while',
					kind: vscode.CompletionItemKind.Keyword,
					insertText: 'while (condition) {\n\t$0\n}',
				}
			];

			return suggestions.map(s => {
				const item = {
					label: s.label,
					kind: s.kind,
					insertText: new vscode.SnippetString(s.insertText),
					insertTextFormat: 2 // Snippet format
				};
				return item as vscode.CompletionItem;
			});
		}
	});
}

// This method is called when your extension is deactivated
export function deactivate() {}
