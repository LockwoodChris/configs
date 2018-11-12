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

print('Overwriting vimrc')
overwrite('./vimrc', '~/.vimrc')
print('Overwriting bashrc')
overwrite('./bashrc', '~/.bashrc')
print('Overwriting tmux')
overwrite('./tmux.conf', '~/.tmux.conf')

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

print('Installing ohmyzsh')
print('----------------------')
print(syscall('sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"'))
print(syscall('chsh -s /bin/zsh/'))
print('Moving zsh config files')
overwrite('./zshrc', '~/.zshrc')
overwrite('./oh-my-zsh-custom.sh', '~/.oh-my-zsh/custom/env_setup.sh')

print('Done')
