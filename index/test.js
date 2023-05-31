

async function main() {
    const mysql = require('mysql2/promise');
    const connection = await mysql.createConnection({ host: 'localhost', user: 'root', database: 'employee', password: "password" });
    var title = ["사원", "대리", "과장", "차장", "부장"]
    var dno = [1, 2, 3, 4]

    for (var i = 0; i <= 10000000; i++) {
        try {
            var employee = {
                empno: i + 1,
                empname: "name" + i,
                title: title[Math.floor(Math.random() * 5)],
                dno: dno[Math.floor(Math.random() * 4)],
                salary: Math.floor(Math.random() * 1000000) + 2000000

            }
            var sql = "insert into employee(empno, empname, title, dno, salary) values(?,?,?,?,?)"
            var params = [employee.empno, employee.empname, employee.title, employee.dno, employee.salary]

            await connection.query(sql, params)
            console.log(i)
        } catch (err) { }

    }
    console.log("success")
    process.exit()
}
main()

