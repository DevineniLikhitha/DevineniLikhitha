<%@page import="java.sql.DriverManager"%>
<%@page import="java.sql.ResultSet"%>
<%@page import="java.sql.Statement"%>
<%@page import="java.sql.Connection"%>
<%
String issueid = request.getParameter("issueid");
String driver = "com.mysql.jdbc.Driver";
String connectionUrl = "jdbc:mysql://localhost:3306/";
String database = "scrumtool";
String userid = "root";
String password = "null";
try {
Class.forName(driver);
} catch (ClassNotFoundException e) {
e.printStackTrace();
}
Connection connection = null;
Statement statement = null;
ResultSet resultSet = null;
%>
<%
try{
connection = DriverManager.getConnection(connectionUrl+database, userid, password);
statement=connection.createStatement();
String sql ="select * from issues where issueid="+issueid;
resultSet = statement.executeQuery(sql);
while(resultSet.next()){
%>
<!DOCTYPE html>
<html>
    <head>
        <style>/*styling from w3 schools-w3schools.com*/
       
        input[type=submit] {
           font-size: 20px;
         padding:5px;
         border-radius: 5px;
         margin: 5px;
         background-color: #04B4AE;
         color: white;
        }
        
        input[type=submit]:hover {
          background-color: #45a049;
        }
        
        div {
          border-radius: 5px;
          background-color: #f2f2f2;
          
        padding: 20px;
        }
        form {
    width: 600px;
    padding: 20px;
    margin: auto;
    background: #CACFD2;
    font-size: 20px; }
        </style>
</head>
    
<body>
<h1>Update Issue Details</h1>
<div>
<form method="post" action="updateissue.jsp">
    ID<br> 
<input type="hidden" name="issueid" value="<%=resultSet.getString("issueid") %>">
<input type="text" name="issueid" value="<%=resultSet.getString("issueid") %>">
<br> </br> 
Issue name:<br>
<input type="text" name="issuename" value="<%=resultSet.getString("issuename") %>">
<br> </br> 
Issue Type:<br>
<input type="text" name="issuetype" value="<%=resultSet.getString("issuetype") %>">
<br> </br> 
Description:<br>
<input type="text" name="issuedescription" value="<%=resultSet.getString("issuedescription") %>">
<br> </br> 

<br> <label for="status">Status:</label><br>
    <select id="type" name="status">
      <option value="To do">To do</option>
      <option value="In progress">In Progress</option>
      <option value="Done">Done</option>
         
    </select>
<!--<input type="text" name="status" value="<%=resultSet.getString("status") %>">-->
<br> </br> 
Sprint No:<br> 
<input type="text" name="sprintid" value="<%=resultSet.getString("sprintid") %>">
<br> </br> 
<input type="submit" value="submit">
</form>
</div>
</body>
<%
}
connection.close();
} catch (Exception e) {
e.printStackTrace();
}
%>

</html>