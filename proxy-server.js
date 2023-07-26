const http = require('http');
const httpProxy = require('http-proxy');

// 后端服务器的地址和端口，替换为您组员的后端地址和端口
const backendHost = 'localhost'; // 后端服务器的主机名或IP地址
const backendPort = 5000; // 后端服务器的端口号

const proxy = httpProxy.createProxyServer();

const server = http.createServer((req, res) => {
  // 设置代理的目标地址
  proxy.web(req, res, { target: `http://${backendHost}:${backendPort}` });
});

server.listen(3000, () => {
  console.log('代理服务器运行在 http://localhost:3000');
});
