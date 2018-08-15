import os
import subprocess

def copy(src, dest):
    os.system('cp ' + src + ' ' + dest)

def delete(f):
    os.system('rm -rf ' + f)

def overwrite(src, dest):
    delete(dest)
    copy(src, dest)

def exists(path):
    return os.path.exists(os.path.expanduser(path))

# Check if there is a vim config
def syscall(string):
    return os.system(string)

print('Copying vimrc')
overwrite('./vimrc', '~/.vimrc')
print('Copying bashrc')
overwrite('./bashrc', '~/.bashrc')
print('Copying tmux')
overwrite('./tmux', '~/.tmux.conf')
print('Copying bash_profile')
overwrite('./bash_profile', '~/.bash_profile')
print('Creating bash_personal if not exists')
syscall('touch ~/.bash_personal')

if not exists('~/.vim'):
    syscall('mkdir ~/.vim')

if not exists('~/.vim/bundle'):
    syscall('mkdir ~/.vim/bundle')

if not exists('~/.vim/bundle/Vundle.vim'):
    print('Installing Vundle')
    print(syscall('git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim'))

if not exists('~/.tmux/plugins/tpm'):
    print(syscall('git clone https://github.com/tmux-plugins/tpm ~/.tmux/plugins/tpm'))
    
print('Installing vim Plugins')
print('----------------------')
print('+ starting install   +')
syscall('vim +PluginInstall +qall')
print('+ updating plugins   +')
print('----------------------')
syscall('vim +PluginUpdate +qall')

print('Installing tmux Plugins')
print('----------------------')
print(syscall('~/.tmux/plugins/tpm/bin/install_plugins'))
print('----------------------')
print('Updating tmux Plugins')
print(syscall('~/.tmux/plugins/tpm/bin/update_plugins all'))

print('Done')
