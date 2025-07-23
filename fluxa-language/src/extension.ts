import * as vscode from 'vscode';

export function activate(context: vscode.ExtensionContext) {
	console.log('Congratulations, your extension "fluxa-language" is now active!');

	const disposable = vscode.commands.registerCommand('fluxa-language.helloWorld', () => {
		vscode.window.showInformationMessage('Hello World from fluxa-language!');
	});
	context.subscriptions.push(disposable);

	const provider = vscode.languages.registerCompletionItemProvider('fluxa', {
		provideCompletionItems(document, position, token, context) {
			const keywords = ['print', 'func', 'def', 'if', 'else', 'for', 'while'];

			return keywords.map(kw => {
				const item = new vscode.CompletionItem(kw, vscode.CompletionItemKind.Keyword);
				item.insertText = kw;
				return item;
			});
		}
	}, '', '.'); // Trigger em qualquer tecla
	context.subscriptions.push(provider);
}

export function deactivate() {}