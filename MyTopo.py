#created by yucong
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.node import OVSSwitch
from mininet.cli import CLI
from mininet.link import TCLink
from mininet.node import OVSBridge
from mininet.term import makeTerm
import sys
import os

class MyTopo(Topo):

	def __init__(self):
	
		Topo.__init__(self)
		
		
		#define the switches
		s1 = self.addSwitch( 's1' )
		s2 = self.addSwitch( 's2' )
		s3 = self.addSwitch( 's3' )
		s4 = self.addSwitch( 's4' )
		s5 = self.addSwitch( 's5' )
		s6 = self.addSwitch( 's6' )
		s7 = self.addSwitch( 's7' )
		s8 = self.addSwitch( 's8' )
		s9 = self.addSwitch( 's9' )
		s10 = self.addSwitch( 's10' )
		bbra = self.addSwitch( 's11')
		bbrb = self.addSwitch( 's12' )
		oz1a = self.addSwitch( 's13' )
		oz1b = self.addSwitch( 's14' )
		oz2a = self.addSwitch( 's15' )
		oz2b = self.addSwitch( 's16' )
		oz3a = self.addSwitch( 's17' )
		oz3b = self.addSwitch( 's18' )
		oz4a = self.addSwitch( 's19' )
		oz4b = self.addSwitch( 's20' )
		oz5a = self.addSwitch( 's21' )
		oz5b = self.addSwitch( 's22' )
		oz6a = self.addSwitch( 's23' )
		oz6b = self.addSwitch( 's24' )
		oz7a = self.addSwitch( 's25' )
		oz7b = self.addSwitch( 's26' )
		
		#add link 
		
		#bbra
		self.addLink( bbra,s1, bw=10 )
		self.addLink( bbra,s2, bw=10)
		self.addLink( bbra,s3, bw=10 )
		self.addLink( bbra,s4, bw=10 )
		self.addLink( bbra,s5, bw=10)
		self.addLink( bbra,bbrb, bw=10)
		self.addLink( bbra,oz4a, bw=10 )
		
		#bbrb
		self.addLink( bbrb,s6, bw=10 )
		self.addLink( bbrb,s7, bw=10 )
		self.addLink( bbrb,s8, bw=10 )
		self.addLink( bbrb,s9, bw=10)
		self.addLink( bbrb,s10, bw=10 )
		self.addLink( bbrb,oz4a, bw=10)
		
		#s1
		self.addLink( s1,oz1b, bw=10 )
		self.addLink( s1,oz5b, bw=10 )
		
		#s2
		self.addLink( s2,oz3a, bw=10 )
		self.addLink( s2,oz4b, bw=10 )
		self.addLink( s2,oz6a , bw=10)
		
		#s3
		self.addLink( s3,oz3b, bw=10 )
		self.addLink( s3,oz6b, bw=10)
		
		#s4
		self.addLink( s4,oz1a, bw=10)
		self.addLink( s4,oz2a, bw=10)
		self.addLink( s4,oz5a, bw=10)
		self.addLink( s4,oz7a, bw=10 )
		
		#s5
		self.addLink( s5,oz2b, bw=10 )
		self.addLink( s5,oz7b, bw=10)
		
		#s6
		self.addLink( s6,oz1b, bw=10)
		self.addLink( s6,oz5b, bw=10)
		
		#s7
		self.addLink( s7,oz3a, bw=10)
		self.addLink( s7,oz6a, bw=10)
		
		#s8
		self.addLink( s8,oz3b, bw=10 )
		self.addLink( s8,oz6b, bw=10 )
		
		#s9
		self.addLink( s9,oz1a , bw=10)
		self.addLink( s9,oz2a, bw=10 )
		self.addLink( s9,oz7a , bw=10)
		
		#s10
		self.addLink( s10,oz2b, bw=10 )
		self.addLink( s10,oz7b, bw=10 )
		
		#bottom
		self.addLink( oz1a,oz1b, bw=10 )
		self.addLink( oz2a,oz2b, bw=10 )
		self.addLink( oz3a,oz3b, bw=10 )
		self.addLink( oz4a,oz4b , bw=10)
		self.addLink( oz5a,oz5b, bw=10 )
		self.addLink( oz6a,oz6b, bw=10 )
		self.addLink( oz7a,oz7b , bw=10)
		
		#host
		h1=self.addHost('h1', ip='100.0.0.1/24')
		h2=self.addHost('h2', ip='100.0.0.2/24')
		h3=self.addHost('h3', ip='100.0.0.3/24')
		h4=self.addHost('h4', ip='100.0.0.4/24')
		
		self.addLink(h1,oz2a,bw=10)
		self.addLink(h2,oz3a,bw=10)
		self.addLink(h3,oz6a,bw=10)
		self.addLink(h4,oz7a,bw=10)
def Phase2():
	c0=RemoteController('c0',ip='127.0.0.1', port=6633)
	net= Mininet(topo=MyTopo(),controller=c0,link=TCLink,switch=OVSSwitch)
	net.start()
	CLI(net)
	net.stop()
	
if __name__=='__main__':
	Phase2()
