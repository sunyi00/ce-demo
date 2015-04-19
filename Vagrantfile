Vagrant.configure(2) do |config|
  (1..1).each do |i|
    nodename = "demonode#{i}"

    config.vm.define nodename do |node|

      node.vm.box = "centos7.1"
      node.vm.hostname = nodename

      node.vm.provider "virtualbox" do |v|
        v.memory = 1024
      end

      node.vm.network "private_network", ip: "192.168.80.2#{i}"

    end

  end

end
