Vagrant.configure('2') do |config|
    config.vm.box = 'hashicorp/bionic64'
    config.vm.provision 'shell',
        path: 'provision.sh',
        privileged: false,
        env: {'STANDALONE' => ENV['STANDALONE']}
    config.vm.provider "virtualbox" do |v|
        v.memory = 8192
        v.cpus = 2
        end
end