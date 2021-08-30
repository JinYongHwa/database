<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
    <%@page import="java.sql.*"%>
    <%@page import="com.mjc.*"%>
    
    <%
    Connection conn=Conn.getInstance();
    ResultSet result=conn.createStatement().executeQuery("select * from users");
    
    
     %>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>

<table>
	<thead>
		<tr>
			<td>아이디</td>
			<td>이름</td>
			<td>패스워드</td>
		</tr>
	</thead>
	<tbody>
	<% while(result.next()){ %>
		<tr>
			<td><%= result.getString("id") %></td>
			<td><%= result.getString("name") %></td>
			<td><%= result.getString("password") %></td>
		</tr>
	<% } %>
	</tbody>
	
</table>
</body>
</html>