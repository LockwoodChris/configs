import os
import subprocess

def copy(src, dest):
    os.system('cp ' + src + ' ' + dest)

def exists(path):
    return os.path.exists(os.path.expanduser(path))

print('Copying vimrc')
copy('./vimrc', '~/.vimrc')
print('Copying bashrc')
copy('./bashrc', '~/.bashrc')
print('Copying tmux')
copy('./tmux', '~/.tmux.conf')
print('Copying bash_profile')
copy('./bash_profile', '~/.bash_profile')

# Check if there is a vim config
def syscall(string):
    return os.system(string)

if exists('~/.vim'):
    syscall('mkdir ~/.vim')

if exists('~/.vim/bundle'):
    syscall('mkdir ~/.vim/bundle')

if exists('~/.vim/bundle/Vundle.vim'):
    print('Installing Vundle')
    print(syscall('git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim'))
    
print('Installing vim Plugins')
print('----------------------')
print('+ starting install   +')
syscall('vim +PluginInstall +qall')

print('Done')

print('Installing tmux Plugins')
print('-----------------------')
print('+ Installing teamocil +')
syscall('gem install --user teamocil')
if not exists('~/.teamocil'):
    syscall('mkdir ~/.teamocil')
