import time, sys
from impacket.dcerpc.v5 import transport

pipes = {
  'atsvc',
  'AudioSrv',
  'browser',
  'cert'
  'Ctx_Winstation_API_Service',
  'DAV RPC SERVICE',
  'db2remotecmd',
  'dnsserver',
  'epmapper',
  'eventlog',
  'HydraLsPipe',
  'InitShutdown',
  'keysvc',
  'locator',
  'llsrpc',
  'lsarpc',
  'lsass',
  'LSM_API_service',
  'netdfs',
  'netlogon',
  'ntsvcs',
  'plugplay',
  'policyagent',
  'ipsec',
  'ProfMapApi',
  'protected_storage',
  'ROUTER',
  'samr',
  'SapiServerPipeS-1-5-5-0-70123',
  'scerpc',
  'SECLOGON',
  'SfcApi',
  'spoolss',
  'srvsvc',
  'ssdpsrv',
  'svcctl',
  'tapsrv'
  'trkwks',
  'W32TIME',
  'W32TIME_ALT',
  'winlogonrpc',
  'winreg',
  'winspipe',
  'wkssvc'
}

if len(sys.argv) != 3:
  print("{} <ip> <port>".format(sys.argv[0]))
  sys.exit(1)

host, port = sys.argv[1],  int(sys.argv[2])

print "[*] pipe-scan 0.1"
print "[*] by p33kab00 (mudnorb@gmail.com)"
print "[*] # of checks: %i\n" %(len(pipes))

start = time.time()*1000
cns = 0
for pipe_name in pipes:
  try:
    stringbinding = "ncacn_np:%s[\pipe\%s]" % (host, pipe_name)  
    trans = transport.DCERPCTransportFactory(stringbinding)
    trans.set_dport(port)
    dce = trans.get_dce_rpc()
    dce.connect()
    print "[+] Found open pipe"
    print "    %s\n" %(pipe_name)
    cns += 1
    dce.disconnect()
  except Exception as e:
    #print('{}: Nope').format(str(e))
    pass

stop = time.time()*1000
print "[*] Found %i open pipes in %i ms." %(cns, int(stop-start))
