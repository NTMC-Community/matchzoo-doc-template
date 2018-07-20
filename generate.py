import os
import sys
import argparse

parser = argparse.ArgumentParser(description='Generate multi-language documents from template.')
parser.add_argument('-l', '--language', help='the language which is used to generate',type=str)
parser.add_argument('-a', '--action', help='generate action',choices=['fbuild','rebuild','update'],type=str)
parser.add_argument('-r', '--rgit', nargs='?', const='rgit',default=None,
                    help='using rgit.sh to add submodule, '\
                         'using this option when your network is not good enough to clone all the submodule.'\
                         'only using this option when action==fbuild')
args = parser.parse_args()
action=args.action
language=args.language
rgit=args.rgit
root_dir = os.path.dirname(os.path.realpath(__file__))
Matchzoo_path = os.path.join(root_dir, 'MatchZoo')
matchzoo_path = os.path.join(Matchzoo_path, 'matchzoo')
doc_path = os.path.join(root_dir, 'docs')
if action == 'fbuild':  # first build
    os.system('git init')
    os.system('git config http.postBuffer 524288000')  # 2000000000
    if rgit=='rgit':
        print('using ResumableGitClone')
        os.system('bash rgit.sh https://github.com/faneshion/MatchZoo')
    else:
        os.system('git submodule add https://github.com/faneshion/MatchZoo')
    os.chdir(Matchzoo_path)
    os.system('git checkout 2.0')
    os.chdir(doc_path)
    os.system('sphinx-apidoc -o ./source ' + matchzoo_path)
    os.system('make gettext')
    os.system('sphinx-intl update -p _build/gettext -l ' + language)
    os.system('sphinx-intl build')
    os.system('sphinx-intl stat')
    os.system('''make -e SPHINXOPTS="-D language='{}'" html'''.format(language))
elif action == 'update':
    os.chdir(doc_path)
    os.system('sphinx-intl build')
    os.system('sphinx-intl stat')
    os.system('make clean')
    os.system('''make -e SPHINXOPTS="-D language='{}'" html'''.format(language))
elif action == 'rebuild':  # main project update
    os.chdir(root_dir)
    os.system('git submodule update --remote')
    os.chdir(doc_path)
    os.system('sphinx-apidoc -f -o ./source ' + matchzoo_path)
    os.system('make gettext')
    os.system('sphinx-intl update -p _build/gettext -l ' + language)
    os.system('sphinx-intl build')
    os.system('sphinx-intl stat')
    os.system('''make -e SPHINXOPTS="-D language='{}'" html'''.format(language))
else:
    print ('wrong action')
