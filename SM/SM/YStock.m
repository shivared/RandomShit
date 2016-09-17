//
//  YStock.m
//  Learning
//
//  Created by Pavan Shivareddy on 3/13/16.
//  Copyright (c) 2016 Pavan Shivareddy. All rights reserved.
//

#import <Foundation/Foundation.h>

#import "YStock.h"
#import "YQLQueryRequest.h"

#define QUERY_PREFIX @"http://query.yahooapis.com/v1/public/yql?q="
#define QUERY_SUFFIX @"&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys&callback="

@implementation YQL

- (NSDictionary *) query: (NSString *)statement {
    NSString *query = [NSString stringWithFormat:@"%@%@%@", QUERY_PREFIX, [statement stringByAddingPercentEscapesUsingEncoding:NSASCIIStringEncoding], QUERY_SUFFIX];
    
    NSData *jsonData = [[NSString stringWithContentsOfURL:[NSURL URLWithString:query] encoding:NSUTF8StringEncoding error:nil] dataUsingEncoding:NSUTF8StringEncoding];
    NSError *error = nil;
    NSDictionary *results = jsonData ? [NSJSONSerialization JSONObjectWithData:jsonData options:0 error:&error] : nil;
    
    if (error) NSLog(@"[%@ %@] JSON error: %@", NSStringFromClass([self class]), NSStringFromSelector(_cmd), error.localizedDescription);
    
    
    return results;
}


@end



//Class Stock Fuction implementation

@implementation Stock

@synthesize Symbol = _Symbol;
//Function
- (float) printStockValue //(NSString *) Symbol
{
    float percentage;
    YQL *yql;
    
    yql = [[YQL alloc] init];
    NSString * Query_Statement = @"select * from yahoo.finance.quotes where symbol=";//\"AAPL\"";
    
    NSString * Query = @"\"";
    Query = [Query_Statement stringByAppendingFormat:@"\"%@\"",_Symbol];
    NSDictionary *results = [yql query:Query];
    NSString * Result = [[results valueForKeyPath:@"query.results"] description];
    NSLog(@"Daily change = %@", [[results valueForKeyPath:@"query.results.quote.PercentChange"] description] );
    NSLog(@"Result = %@",Result);
    percentage = [[[results valueForKeyPath:@"query.results.quote.PercentChange"] description] floatValue];
    return percentage;
}

@end
