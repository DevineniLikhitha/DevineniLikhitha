<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
pageEncoding="ISO-8859-1"%>
<%@page import="java.sql.*,java.util.*"%>

<%

String sprintname=request.getParameter("sprintname");
String startdate=request.getParameter("startdate");
String enddate=request.getParameter("enddate");


try
{
Class.forName("com.mysql.jdbc.Driver");
Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/scrumtool", "root", "null");
Statement st=conn.createStatement();

int i=st.executeUpdate("insert into sprints(sprintname,startdate,enddate)values('"+sprintname+"','"+startdate+"','"+enddate+"')");
        out.println("Data is successfully inserted!");

        }
catch(Exception e)
{
System.out.print(e);
e.printStackTrace();
}
%>