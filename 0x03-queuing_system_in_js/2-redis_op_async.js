import { createClient, print } from 'redis';
const util = require('util');

const client = createClient();

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

const setNewSchool = function (schoolName, value) {
  client.set(schoolName, value, print);
};

const displaySchoolValue = async function (schoolName) {
  console.log(await util.promisify(client.get).bind(client)(schoolName));
};

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
