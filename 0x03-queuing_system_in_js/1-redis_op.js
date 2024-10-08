import { createClient } from 'redis';

const client = await createClient()
  .on('error', err => console.log('Redis client not connected to the server:', err))
  .connect();
console.log('Redis client connected to the server');

function setNewSchool (schoolName, value) {
  client.set(schoolName, value);
  redis.print('Done');
}

function displaySchoolValue(schoolName) {
  console.log(client.get(schoolName));
}


displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
