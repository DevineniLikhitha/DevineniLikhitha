<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
pageEncoding="ISO-8859-1"%>
<%@page import="java.sql.*,java.util.*"%>

<%
//String issueid=request.getParameter("issueid");
String issuename=request.getParameter("issuename");
String issuetype=request.getParameter("issuetype");
String issuedescription=request.getParameter("issuedescription");

 String status=request.getParameter("status");
String sprintid=request.getParameter("sprintid");
try
{
Class.forName("com.mysql.jdbc.Driver");
Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/scrumtool", "root", "null");
Statement st=conn.createStatement();
int i=st.executeUpdate("insert into issues(issuename,issuetype,issuedescription,status,sprintid)values('"+issuename+"','"+issuetype+"','"+issuedescription+"','"+status+"','"+sprintid+"')");
        out.println("Data is successfully inserted!");
        }
catch(Exception e)
{
System.out.print(e);
e.printStackTrace();
}
%>