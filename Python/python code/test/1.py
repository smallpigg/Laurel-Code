class HttpParser extends Base {
 
public function __construct(){
 }
 
function getContentByCurl($url, $headers=array(), $binary=false ) {
 
$curlHandler = curl_init();
 $cookie_file = dirname(__FILE__) . "/googlecookie.txt";
 curl_setopt($curlHandler, CURLOPT_URL, $url);
 curl_setopt($curlHandler, CURLOPT_TIMEOUT, 5);
 // headers like: array('Content-type: text/plain', 'Content-length: 100')
 curl_setopt($curlHandler, CURLOPT_HTTPHEADER, $headers);//not need header
 curl_setopt($curlHandler, CURLOPT_HEADER, false);//not need header
 curl_setopt($curlHandler, CURLOPT_RETURNTRANSFER, 1); //return contents
 curl_setopt($curlHandler, CURLOPT_FOLLOWLOCATION, 1);// allow redirects
 curl_setopt($curlHandler, CURLOPT_COOKIEJAR, $cookie_file);
 curl_setopt($curlHandler, CURLOPT_USERAGENT, array_rand(
 array(
 "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
 "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.97 Safari/537.11",
 ))
 );
 if( false!==(stripos($url,"https://")) ){
 curl_setopt($curlHandler, CURLOPT_SSL_VERIFYPEER, false); //need for https
 curl_setopt($curlHandler, CURLOPT_SSL_VERIFYHOST, false); //need for https
 }
 curl_setopt($curlHandler, CURLOPT_BINARYTRANSFER, $binary);
 //curl_setopt($curlHandler, CURLOPT_FILE, $fileOutput);
 $contents = curl_exec($curlHandler);
 return $contents;
 }
 
public function getContent($url){
 $contents = file_get_contents($url);
 return $contents;
 }
 
public function parse($url,$callback=false){
 $content = $this->getContent($url);
 if ( $callback )
 $content = call_user_func( $callback, $content );
 return $content;
 }
}