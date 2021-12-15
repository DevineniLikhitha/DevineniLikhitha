package org.apache.jsp;

import javax.servlet.*;
import javax.servlet.http.*;
import javax.servlet.jsp.*;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;
import java.sql.Connection;

public final class viewissues_jsp extends org.apache.jasper.runtime.HttpJspBase
    implements org.apache.jasper.runtime.JspSourceDependent {

  private static final JspFactory _jspxFactory = JspFactory.getDefaultFactory();

  private static java.util.List<String> _jspx_dependants;

  private org.glassfish.jsp.api.ResourceInjector _jspx_resourceInjector;

  public java.util.List<String> getDependants() {
    return _jspx_dependants;
  }

  public void _jspService(HttpServletRequest request, HttpServletResponse response)
        throws java.io.IOException, ServletException {

    PageContext pageContext = null;
    HttpSession session = null;
    ServletContext application = null;
    ServletConfig config = null;
    JspWriter out = null;
    Object page = this;
    JspWriter _jspx_out = null;
    PageContext _jspx_page_context = null;

    try {
      response.setContentType("text/html");
      pageContext = _jspxFactory.getPageContext(this, request, response,
      			null, true, 8192, true);
      _jspx_page_context = pageContext;
      application = pageContext.getServletContext();
      config = pageContext.getServletConfig();
      session = pageContext.getSession();
      out = pageContext.getOut();
      _jspx_out = out;
      _jspx_resourceInjector = (org.glassfish.jsp.api.ResourceInjector) application.getAttribute("com.sun.appserv.jsp.resource.injector");

      out.write("\n");
      out.write("\n");
      out.write("\n");
      out.write("\n");

String id = request.getParameter("userid");
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

      out.write("\n");
      out.write("<!DOCTYPE html>\n");
      out.write("<html>\n");
      out.write("    <head> \n");
      out.write("    <meta charset = \"utf-8\">\n");
      out.write("    <title> view issues</title>\n");
      out.write("    <meta name=\"viewport\" content =\"width=device-width, initial- scale=1.0\">\n");
      out.write("     \n");
      out.write("    <link rel=\"stylesheet\" href=\"style.css\">\n");
      out.write("   \n");
      out.write("\n");
      out.write("    <style>\n");
      out.write("       \n");
      out.write("        *{\n");
      out.write("            padding: 0;\n");
      out.write("            margin: 0;\n");
      out.write("            text-decoration: none;\n");
      out.write("            list-style: none;\n");
      out.write("           /* text-align: right; */\n");
      out.write("          }\n");
      out.write("          body {\n");
      out.write("              font-family: Arial, Helvetica, sans-serif;\n");
      out.write("              }\n");
      out.write("              nav{\n");
      out.write("                  height: 80px;\n");
      out.write("                  width: 100%;\n");
      out.write("                  background: #04B4AE;\n");
      out.write("              }    \n");
      out.write("              nav li {\n");
      out.write("                  \n");
      out.write("                  display: inline-block;\n");
      out.write("                  margin:  0 8px;\n");
      out.write("                  line-height: 80px;\n");
      out.write("                  \n");
      out.write("              }\n");
      out.write("              nav a{\n");
      out.write("                  color: white;\n");
      out.write("                  font-size: 18px;\n");
      out.write("                  \n");
      out.write("                  \n");
      out.write("              }\n");
      out.write(" #issues {\n");
      out.write("  font-family: Arial, Helvetica, sans-serif;\n");
      out.write("  border-collapse: collapse;\n");
      out.write("  width: 100%;\n");
      out.write("}\n");
      out.write("\n");
      out.write("#issues td, #issues th {\n");
      out.write("  border: 1px solid #ddd;\n");
      out.write("  padding: 8px;\n");
      out.write("}\n");
      out.write("\n");
      out.write("#issues tr:nth-child(even){background-color: #f2f2f2;}\n");
      out.write("\n");
      out.write("#issues tr:hover {background-color: #ddd;}\n");
      out.write("\n");
      out.write("#issues th {\n");
      out.write("  padding-top: 12px;\n");
      out.write("  padding-bottom: 12px;\n");
      out.write("  text-align: left;\n");
      out.write("  background-color: #04B4AE; \n");
      out.write("  color: white;\n");
      out.write("}\n");
      out.write(" .button{\n");
      out.write("              height:55px;\n");
      out.write("              width:100px;\n");
      out.write("              margin: 5px;\n");
      out.write("              background-color: #04B4AE; \n");
      out.write("              color: white;\n");
      out.write("              \n");
      out.write("    \n");
      out.write("    </style>\n");
      out.write("    </head>\n");
      out.write("<body>\n");
      out.write(" <nav>\n");
      out.write("      \n");
      out.write("        \n");
      out.write("\n");
      out.write("     <label class = \"logo\">  </label> \n");
      out.write("    <ul>\n");
      out.write("         <li><a href=\"Home.html\">Home</a></li>\n");
      out.write("       \n");
      out.write("        <li><a href=\"Project1.html\">Projects</a></li>\n");
      out.write("        \n");
      out.write("        <li><a href=\"sprint.html\">Sprints</a></li>\n");
      out.write("        <li><a href=\"viewissues.jsp\">Product Backlog</a></li>\n");
      out.write("        <li><a href=\"viewsprintbacklog.jsp\">Sprint Backlog</a></li>\n");
      out.write("        <li><a href=\"issues.html\">Issues</a></li>\n");
      out.write("           <li style=\"float:right\"><a href=\"Login.html\">Logout</a></li>\n");
      out.write("    \n");
      out.write("    </ul><br><br>\n");
      out.write("     <center><h1>Issues</h1></center><br><br>\n");
      out.write("<table id=\"issues\">\n");
      out.write("\n");
      out.write("<tr>\n");
      out.write("<th style=\"text-align: center;\">Issue Id</th>\n");
      out.write("<th style=\"text-align: center;\">Issue Name</th>\n");
      out.write("<th style=\"text-align: center;\">Issue Type</th>\n");
      out.write("<th style=\"text-align: center;\">Description</th>\n");
      out.write("\n");
      out.write("<th style=\"text-align: center;\">Status</th>\n");
      out.write("<th style=\"text-align: center;\">Sprint ID</th>\n");
      out.write("<th style=\"text-align: center;\">Update</th>\n");
      out.write("\n");
      out.write("\n");
      out.write("\n");
      out.write("</tr>\n");

try{
connection = DriverManager.getConnection(connectionUrl+database, userid, password);
statement=connection.createStatement();
String sql ="select * from issues";
resultSet = statement.executeQuery(sql);
while(resultSet.next()){

      out.write("\n");
      out.write("<center>\n");
      out.write("<tr>\n");
      out.write("<td style = \"text-align: center;\">");
      out.print(resultSet.getString("issueid") );
      out.write("</td>\n");
      out.write("<td style=\"text-align: center;\">");
      out.print(resultSet.getString("issuename") );
      out.write("</td>\n");
      out.write("<td style=\"text-align: center;\">");
      out.print(resultSet.getString("issuetype") );
      out.write("</td>\n");
      out.write("<td style=\"text-align: center;\">");
      out.print(resultSet.getString("issuedescription") );
      out.write("</td>\n");
      out.write("\n");
      out.write("<td style=\"text-align: center;\">");
      out.print(resultSet.getString("status") );
      out.write("</td>\n");
      out.write("\n");
      out.write("\n");
      out.write("<td> <button class=\"button\"> <a href=\"updateissueform.jsp?issueid=");
      out.print(resultSet.getString("issueid"));
      out.write("\">update</a></button></td>\n");
      out.write("</tr></center>\n");

}
connection.close();
} catch (Exception e) {
e.printStackTrace();
}

      out.write("\n");
      out.write("</table>\n");
      out.write(" </nav>\n");
      out.write("</body>\n");
      out.write("</html>");
    } catch (Throwable t) {
      if (!(t instanceof SkipPageException)){
        out = _jspx_out;
        if (out != null && out.getBufferSize() != 0)
          out.clearBuffer();
        if (_jspx_page_context != null) _jspx_page_context.handlePageException(t);
        else throw new ServletException(t);
      }
    } finally {
      _jspxFactory.releasePageContext(_jspx_page_context);
    }
  }
}
