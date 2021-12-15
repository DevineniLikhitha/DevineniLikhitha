<%@ page language="java" contentType="text/html; charset=ISO-8859-1" pageEncoding="ISO-8859-1"%>
<%@ page import="java.sql.*" %>
<%! String driverName = "com.mysql.jdbc.Driver";%>
<%!String url = "jdbc:mysql://localhost:3306/scrumtool";%>
<%!String user = "root";%>
<%!String psw = "null";%>
<%
String issueid = request.getParameter("issueid");
String issuename=request.getParameter("issuename");
String issuetype=request.getParameter("issuetype");
String issuedescription=request.getParameter("issuedescription");

String status=request.getParameter("status");
String sprintid=request.getParameter("sprintid");
if(issueid != null)
{
Connection con = null;
PreparedStatement ps = null;
int issueID = Integer.parseInt(issueid);
try
{
Class.forName(driverName);
con = DriverManager.getConnection(url,user,psw);
String sql="Update issues set issueid=?,issuename=?,issuetype=?,issuedescription=?,status=?,sprintid=? where issueid="+issueid;
ps = con.prepareStatement(sql);
ps.setString(1,issueid);
ps.setString(2, issuename);
ps.setString(3, issuetype);
ps.setString(4, issuedescription);

ps.setString(5,status);
ps.setString(6,sprintid);

int i = ps.executeUpdate();
if(i > 0)
{
out.print("Record Updated Successfully");
}
else
{
out.print("There is a problem in updating Record.");
}
}
catch(SQLException sql)
{
request.setAttribute("error", sql);
out.println(sql);
}
}
%>