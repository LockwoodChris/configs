import os

def copy(src, dest):
    os.system('cp ' + src + ' ' + dest)

print('Copying vimrc')
copy('./vimrc', '~/.vimrc')
print('Copying bashrc')
copy('./bashrc', '~/.bashrc')
print('Copying tmux')
copy('./tmux', '~/.tmux.conf')

# Check if there is a vim config
def syscall(string):
    return os.system(string)

if syscall('test -d ~/.vim') != 0:
    if syscall('test -d ~/.vim/bundle') != 0:
        if syscall('test -f ~/.vim/bundle/Vundle.vim') != 0:
            print('Installing Vundle')
            print(syscall('git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim'))
            
print('Installing vim Plugins')
syscall('vim +PluginInstall +qall')

print('Done')
