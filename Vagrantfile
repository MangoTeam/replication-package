Vagrant.configure('2') do |config|
    config.vm.box = 'hashicorp/bionic64'
    config.vm.provision 'shell', 
        path: 'provision.sh',
        privileged: false,
        env: {'STANDALONE' => ENV['STANDALONE']}
end